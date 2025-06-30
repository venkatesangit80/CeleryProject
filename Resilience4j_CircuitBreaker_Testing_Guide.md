# ✅ Smart Testing of Resilience4j Circuit Breaker (Without Chaos Monkey)

This guide outlines a simple, non-intrusive way to test and provide evidence for a Resilience4j Circuit Breaker implementation without needing Chaos Engineering tools like Chaos Monkey.

---

## 1️⃣ Confirm Circuit Breaker Configuration

Ensure your configuration is correct in `application.yml` or Java:

```yaml
resilience4j.circuitbreaker:
  instances:
    myService:
      failureRateThreshold: 50
      minimumNumberOfCalls: 5
      waitDurationInOpenState: 10s
      slidingWindowSize: 10
```

Or via Java config:

```java
CircuitBreakerConfig config = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)
    .minimumNumberOfCalls(5)
    .waitDurationInOpenState(Duration.ofSeconds(10))
    .slidingWindowSize(10)
    .build();
```

---

## 2️⃣ Trigger Failures to Simulate Circuit Breaker Tripping

Create a loop to simulate failures programmatically:

```java
for (int i = 0; i < 6; i++) {
  try {
    myServiceClient.callWithExpectedFailure(); // force failures
  } catch (Exception e) {
    // expected
  }
}
```

This will trip the Circuit Breaker from `CLOSED` → `OPEN` state when the failure rate exceeds threshold.

---

## 3️⃣ Check Circuit Breaker State

Use Resilience4j’s API to inspect the state:

```java
CircuitBreaker cb = CircuitBreakerRegistry.ofDefaults().circuitBreaker("myService");
System.out.println(cb.getState()); // Should print: OPEN
```

---

## 4️⃣ Evidence Collection

| Evidence Type            | What to Capture                                                  |
|--------------------------|------------------------------------------------------------------|
| ✅ Unit Test Screenshot  | Showing CB moving from CLOSED → OPEN                            |
| ✅ Logs                  | Look for `CircuitBreaker 'myService' changed state to OPEN`     |
| ✅ Actuator Endpoint     | `/actuator/circuitbreakers/myService` → `"state": "OPEN"`       |
| ✅ Grafana (optional)    | CircuitBreaker metrics if Prometheus is integrated              |

---

## 5️⃣ Optional: JUnit Proof-of-Concept

```java
@Test
public void testCircuitBreakerOpensOnFailures() {
    CircuitBreaker cb = registry.circuitBreaker("myService");
    for (int i = 0; i < 6; i++) {
        Try.of(cb.decorateCheckedSupplier(() -> {
            throw new RuntimeException("fail");
        }));
    }
    assertEquals(CircuitBreaker.State.OPEN, cb.getState());
}
```

---

## ✅ Summary

- Simulate failures using code (no chaos testing needed)
- Confirm Circuit Breaker state transition via API/logs
- Collect screenshots/logs for evidence
- Bonus: validate `HALF_OPEN → CLOSED` recovery after wait duration

Let us know if you need:
- A sample Spring Boot test class
- Markdown table for reporting
- Prometheus dashboard integration
