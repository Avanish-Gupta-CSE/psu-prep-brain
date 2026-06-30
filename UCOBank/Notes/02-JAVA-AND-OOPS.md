# 02. Java & Object-Oriented Programming (OOPs)

This note covers core Java and OOP concepts with a focus on enterprise banking architectures. It also provides a conceptual bridge from your JavaScript/TypeScript experience to Spring Boot.

---

## 1. The 4 Pillars of OOPs (With Banking Examples)

Object-Oriented Programming (OOP) is a paradigm based on the concept of "objects" containing data and code.

### 1. Encapsulation (Data Hiding)
*   **Definition**: Wrapping data (variables) and code (methods) together as a single unit, and restricting direct access to the inner workings of that unit.
*   **Banking Example**: An `Account` class should hide its `balance` variable. It must be marked `private` so external classes cannot modify it directly (e.g., `acc.balance = -500`). Instead, modifications must go through public methods like `deposit()` and `withdraw()`, which contain validation logic.
```java
public class Account {
    private double balance; // Encapsulated data

    public double getBalance() {
        return this.balance;
    }

    public void withdraw(double amount) throws InsufficientBalanceException {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        if (this.balance < amount) {
            throw new InsufficientBalanceException("Insufficient funds");
        }
        this.balance -= amount; // Controlled modification
    }
}
```

### 2. Abstraction (Implementation Hiding)
*   **Definition**: Hiding internal implementation details and showing only essential features to the user.
*   **Banking Example**: A `PaymentProcessor` interface defines a `processPayment()` method. The calling class doesn't need to know whether the payment is processed via UPI, NEFT, or RTGS. It just calls the interface method.
```java
public interface PaymentProcessor {
    void processPayment(double amount, String recipientAccount);
}

public class UPIProcessor implements PaymentProcessor {
    public void processPayment(double amount, String recipientAccount) {
        // Complex low-level NPCI API calls and cryptographic signing
    }
}
```

### 3. Inheritance (Code Reusability)
*   **Definition**: The mechanism by which one class (child/subclass) acquires the properties and behaviors of another class (parent/superclass).
*   **Banking Example**: A generic `Account` class holds common properties like `accountId` and `balance`. Specific account types like `SavingsAccount` (which has an `interestRate`) and `CurrentAccount` (which has an `overdraftLimit`) inherit from `Account`.
```java
public class SavingsAccount extends Account {
    private double interestRate;

    public void applyInterest() {
        double interest = getBalance() * (interestRate / 100);
        deposit(interest);
    }
}
```

### 4. Polymorphism (Many Forms)
*   **Definition**: The ability of a single message, method, or object to behave differently in different contexts.
*   **Compile-time Polymorphism (Method Overloading)**: Same method name, different parameter signatures.
    *   *Example*: `transfer(double amount, String accountNo)` vs. `transfer(double amount, String accountNo, String remarks)`.
*   **Runtime Polymorphism (Method Overriding)**: A child class provides a specific implementation of a method already defined in its parent class.
    *   *Example*: Overriding a `calculateCharges()` method. A `SavingsAccount` might have zero charges, while a `CurrentAccount` might charge a fee if the balance drops below the overdraft limit.

---

## 2. Java Collections Framework

The Collections framework is a unified architecture for representing and manipulating collections of data.

```
                  Collection (Interface)
                 /          |         \
         List (I)        Set (I)     Queue (I)
        /     \            |
   ArrayList LinkedList  HashSet
                           |
                         LinkedHashSet
                         
                  Map (Interface) -- (Not a child of Collection)
                 /       |       \
            HashMap  LinkedHashMap TreeMap
```

### Key Collection Types & Banking Use Cases:

#### 1. List (Ordered, Allows Duplicates)
*   **ArrayList**: Resizable array. Fast $O(1)$ random access by index. Slow $O(N)$ insertions/deletions in the middle because elements must be shifted.
    *   *Banking Use Case*: Storing a list of transaction records retrieved from a database to display on a screen.
*   **LinkedList**: Doubly-linked list. Fast $O(1)$ insertions/deletions at any position (once the node is found). Slow $O(N)$ search.
    *   *Banking Use Case*: Implementing a FIFO transaction queue for sequential processing.

#### 2. Set (Unordered, Unique Elements)
*   **HashSet**: Backed by a HashMap. Fast $O(1)$ search, insertion, and deletion. No order guaranteed.
    *   *Banking Use Case*: Storing a set of unique active login session IDs to prevent duplicate logins.
*   **TreeSet**: Backed by a Red-Black Tree. Elements are stored in sorted order. $O(\log N)$ search, insertion, and deletion.

#### 3. Map (Key-Value Pairs)
*   **HashMap**: Stores key-value pairs. Fast $O(1)$ average-case search, insertion, and deletion.
    *   *HashMap Internals (Crucial Interview Question)*:
        *   Uses a technique called **Hashing** to map keys to bucket locations.
        *   If two different keys produce the same hash code, a **Collision** occurs.
        *   Java handles collisions using **Chaining**: buckets are linked lists.
        *   In Java 8+, if a bucket's linked list grows past a threshold (8 elements), it is converted into a **Balanced Red-Black Tree**, improving worst-case search time from $O(N)$ to $O(\log N)$.
*   **ConcurrentHashMap**: A thread-safe Map. Unlike `Hashtable` (which locks the entire map, causing severe bottlenecks), `ConcurrentHashMap` uses **Bucket-level locking** (segment-level locking in older Java versions). Multiple threads can read and write to different buckets concurrently without blocking each other.
    *   *Banking Use Case*: In-memory cache for storing active currency exchange rates that are updated by background threads and read by thousands of concurrent user transactions.

---

## 3. Multithreading & Concurrency in Java

Multithreading is the concurrent execution of multiple parts of a program (threads) to maximize CPU utilization. In banking, multithreading is essential for handling thousands of concurrent transaction requests.

### Thread vs. Runnable
*   **Thread Class**: Inheriting from `Thread` class. (Limits inheritance since Java doesn't support multiple inheritance).
*   **Runnable Interface**: Implementing `Runnable` and passing it to a `Thread` object. (Preferred, as it allows inheritance from other classes).

### Thread Safety & Synchronization
When multiple threads access shared mutable data (e.g., modifying an account balance), it can lead to a **Race Condition**.
*   **Synchronized Keyword**: Locks an object or method so only one thread can execute it at a time.
```java
public synchronized void deposit(double amount) {
    this.balance += amount; // Thread-safe
}
```
*   **Volatile Keyword**: Ensures that changes to a variable are immediately visible to all threads by reading/writing directly to main memory instead of the CPU cache. It does *not* guarantee atomicity.
*   **Atomic Variables (e.g., `AtomicInteger`, `AtomicDouble`)**: Use low-level CPU instructions like **Compare-And-Swap (CAS)** to perform lock-free, atomic operations. Highly efficient.

### Deadlocks
*   **What is it?** A situation where Thread 1 holds Lock A and waits for Lock B, while Thread 2 holds Lock B and waits for Lock A. Both threads are blocked forever.
*   **Deadlock Prevention in Banking**:
    *   *The Problem*: Transferring money between two accounts. Thread 1 locks Account A then tries to lock Account B. Thread 2 concurrently locks Account B then tries to lock Account A.
    *   *The Solution*: Always acquire locks in a strict, deterministic order (e.g., sort the lock acquisitions by `accountId`).
```java
public void transfer(Account from, Account to, double amount) {
    Account firstLock = from.getAccountId() < to.getAccountId() ? from : to;
    Account secondLock = from.getAccountId() < to.getAccountId() ? to : from;

    synchronized(firstLock) {
        synchronized(secondLock) {
            from.withdraw(amount);
            to.deposit(amount);
        }
    }
}
```

---

## 4. Exception Handling in Java

Java divides exceptions into two main categories:

```
                     Throwable
                    /         \
             Error             Exception
                              /         \
                      IOException     RuntimeException
                      (Checked)       (Unchecked)
```

1.  **Checked Exceptions (Compile-time)**: Checked by the compiler. The developer *must* handle them using `try-catch` or declare them in the method signature using `throws`.
    *   *Examples*: `SQLException`, `IOException`.
2.  **Unchecked Exceptions (Runtime)**: Occur at runtime. Not checked by the compiler. Usually indicate programming errors.
    *   *Examples*: `NullPointerException`, `ArithmeticException`, `IllegalArgumentException`.

### Custom Banking Exceptions
Always create custom exceptions to handle business logic failures gracefully.
```java
public class InsufficientBalanceException extends Exception {
    public InsufficientBalanceException(String message) {
        super(message);
    }
}
```

---

## 5. Bridging Node.js to Spring Boot (For the Interview)

Since your primary production experience is in Node.js, the panel might ask how you will transition to Spring Boot. Use this conceptual mapping to show that you understand the architectural equivalence:

| Concept | Node.js / Express Stack | Java / Spring Boot Stack |
| :--- | :--- | :--- |
| **Runtime Environment** | V8 Engine (Single-threaded Event Loop) | JVM (Multi-threaded Thread-Per-Request) |
| **Web Framework** | Express.js | Spring Web / Spring MVC |
| **Routing & Controllers** | `router.get('/accounts', controller)` | `@RestController` with `@GetMapping("/accounts")` |
| **Dependency Injection** | Manual imports or Awilix | Spring IoC Container with `@Autowired` / `@Component` |
| **Database ORM** | Sequelize / Knex / Prisma | Spring Data JPA / Hibernate |
| **Security Middleware** | Passport.js / Keycloak-connect | Spring Security |
| **Build Tool / Package Mgr**| npm / yarn | Maven / Gradle |

### How to Pitch This:
> "While Node.js and Spring Boot have different runtime models—Node.js using a single-threaded asynchronous event loop and Spring Boot traditionally using a thread-per-request model—they solve the exact same enterprise problems. 
>
> In Express, I use middleware for authentication, controllers for routing, and Knex or Prisma for database queries. In Spring Boot, I use Spring Security filters, `@RestController` classes, and Spring Data JPA repositories. Because I have built production-grade, secure microservices at Berkadia, I already master the underlying architectural patterns. Transitioning to Spring Boot syntax is simply a matter of mapping these patterns to Spring annotations."
