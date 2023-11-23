Composition in OOP is the process of creating a new object by using other existing objects. This allows you to create complex objects from simpler objects.

**Example:**

Consider a car class. A car is made up of many different parts, such as an engine, transmission, wheels, and tires. We can create a car class by composing it of the other parts.

```python
class Engine:
    def start(self):
        pass

    def stop(self):
        pass

class Transmission:
    def shift_gear(self, gear):
        pass

class Wheel:
    def rotate(self):
        pass

class Tire:
    def roll(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine()
        self.transmission = Transmission()
        self.wheels = [Wheel() for i in range(4)]
        self.tires = [Tire() for i in range(4)]

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def shift_gear(self, gear):
        self.transmission.shift_gear(gear)

    def accelerate(self):
        for wheel in self.wheels:
            wheel.rotate()
```

In the above example, the Car class is composed of the Engine, Transmission, Wheel, and Tire classes. This allows us to create a complex object (a car) from simpler objects.

**Uses cases of composition:**

Composition is used in a wide variety of software applications, including:

* Graphical user interfaces (GUIs): GUIs are often composed of many different widgets, such as buttons, labels, and text boxes.
* Web applications: Web applications are often composed of many different components, such as headers, footers, and navigation bars.
* Database applications: Database applications are often composed of many different objects, such as tables, columns, and rows.
* Operating systems: Operating systems are often composed of many different components, such as the kernel, the device drivers, and the system libraries.

**Benefits of composition:**

Composition offers a number of benefits, including:

* Reusability: Composition allows us to reuse code by composing existing objects into new objects.
* Modularity: Composition makes the code more modular and easier to maintain.
* Encapsulation: Composition allows us to encapsulate the complexity of a complex object within a simpler object.

**Benchmarks of composition:**

Composition is a well-established design principle in OOP. It is used in a wide variety of successful software applications.

## Conclusion

Composition is a powerful tool that can be used to improve the design and quality of your code. It allows you to create complex objects from simpler objects, reuse code, make the code more modular, and encapsulate the complexity of a complex object within a simpler object.

Here are some additional benefits of composition:

* **Flexibility:** Composition makes the code more flexible and adaptable to changes. For example, if we need to change the way that a car accelerates, we can simply change the implementation of the Wheel class. We do not need to change the Car class itself.
* **Testability:** Composition makes the code more testable. We can test the individual components of a complex object in isolation. This makes it easier to identify and fix bugs.

Overall, composition is a valuable tool that can be used to improve the design, quality, flexibility, and testability of your code.

## Compositions vs Inheritance:

Composition and inheritance are two important concepts in object-oriented programming (OOP). They are both used to create new objects, but they do so in different ways.

**Composition** is the process of creating a new object by using other existing objects. This allows you to create complex objects from simpler objects.

**Inheritance** is the process of creating a new object that is based on an existing object. This allows you to reuse code and create hierarchies of objects.

Here is a table that summarizes the key differences between composition and inheritance:

| Characteristic | Composition | Inheritance |
|---|---|---|
| Definition | Creates a new object by using other existing objects. | Creates a new object that is based on an existing object. |
| Relationship | Has-a relationship (e.g., a car has a wheel). | Is-a relationship (e.g., a car is a vehicle). |
| Code reuse | Achieved by composing existing objects into new objects. | Achieved by inheriting code from a base class. |
| Flexibility | More flexible than inheritance, as it allows you to combine objects in different ways. | Less flexible than composition, as it is more difficult to change the behavior of inherited classes. |
| Use cases | Used to create complex objects from simpler objects, and to reuse code. | Used to create hierarchies of objects, and to reuse code. |

**Example of composition:**

```python
class Wheel:
    def rotate(self):
        pass

class Car:
    def __init__(self):
        self.wheels = [Wheel() for i in range(4)]

    def accelerate(self):
        for wheel in self.wheels:
            wheel.rotate()
```

In the above example, the Car class is composed of the Wheel class. The Car class has a has-a relationship with the Wheel class. This means that a Car object has one or more Wheel objects.

**Example of inheritance:**

```python
class Vehicle:
    def accelerate(self):
        pass

class Car(Vehicle):
    def accelerate(self):
        # Call the accelerate() method of the base class.
        super().accelerate()

        # Additional code to accelerate the car.
        pass
```

In the above example, the Car class inherits from the Vehicle class. The Car class is-a Vehicle. This means that a Car object has all of the properties and behaviors of a Vehicle object.

**Composition vs inheritance in practice**

Composition is generally preferred over inheritance, because it is more flexible and less likely to lead to problems such as tight coupling and fragility. However, there are some cases where inheritance is more appropriate, such as when you need to create hierarchies of objects or reuse code from a base class.

Here is a general rule of thumb:

* Use composition when you need to create a new object that has-a relationship with other existing objects.
* Use inheritance when you need to create a new object that is-a specialized type of an existing object.

## Which Should I choose when?

**Composition** should be preferred over **inheritance** in most cases. It is a more flexible and less error-prone way to design object-oriented programs.

**When to use composition:**

* When you need to create a new object that has-a relationship with other existing objects. For example, a Car object has-a Engine object.
* When you need to combine objects in different ways to create new functionality. For example, a Car object can be combined with a Trailer object to create a Truck object.
* When you need to reuse code by composing existing objects into new objects. For example, you can reuse the Engine object in both a Car object and a Truck object.

**When to use inheritance:**

* When you need to create a new object that is-a specialized type of an existing object. For example, a SportsCar object is-a specialized type of Car object.
* When you need to reuse code from a base class in derived classes. For example, you can reuse the accelerate() method from the Vehicle class in the Car class.
* When you need to create hierarchies of objects. For example, you can create a hierarchy of Vehicle objects, including Car, Truck, and Motorcycle objects.

**Advantages of composition over inheritance:**

* Composition is more flexible than inheritance. It allows you to combine objects in different ways to create new functionality.
* Composition is less error-prone than inheritance. It is less likely to lead to problems such as tight coupling and fragility.
* Composition makes your code more testable. You can test the individual components of a complex object in isolation.

**Overall, composition is a more powerful and flexible tool than inheritance. It is the preferred way to design object-oriented programs.**