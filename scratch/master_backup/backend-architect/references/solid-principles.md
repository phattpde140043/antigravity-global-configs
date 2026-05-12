# SOLID Principles

The 5 principles of object-oriented design that make code more flexible, maintainable, and understandable.

## 1. SRP: Single Responsibility Principle
*A module should have one, and only one, reason to change (one actor).*
- If a class handles both DB persistence and business logic, it has two actors. Split it.

## 2. OCP: Open-Closed Principle
*A software artifact should be open for extension but closed for modification.*
- Use interfaces and abstractions so you can add new behavior by adding new classes, not by changing old ones.

## 3. LSP: Liskov Substitution Principle
*Subtypes must be substitutable for their base types.*
- If you override a method, don't change its expected behavior. Don't throw "NotImplementedException" if the base class says it's supported.

## 4. ISP: Interface Segregation Principle
*Many client-specific interfaces are better than one general-purpose interface.*
- Don't force a class to depend on methods it doesn't use. Split large interfaces into smaller, focused ones.

## 5. DIP: Dependency Inversion Principle
*Depend on abstractions, not on concretions.*
- The high-level policy should not depend on low-level details. Both should depend on abstractions (interfaces).
