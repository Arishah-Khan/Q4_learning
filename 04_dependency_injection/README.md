# Dependency Injection in FastAPI

## What is Dependency Injection?

Dependency Injection (DI) is a way to manage common tasks that need to be used across different parts of your application, such as checking if a user is logged in or connecting to a database. Instead of repeating the same code everywhere, you write it once and use it wherever it's needed.

## Why Use Dependency Injection?

1. **Reuse Code**: Write code once and reuse it in multiple places.
2. **Cleaner Code**: DI helps keep your endpoint logic focused on its task, while common tasks (like authentication) are handled separately.
3. **Easier Testing**: You can replace real dependencies with mock versions when testing your application.
4. **Organized Code**: Keeps your codebase neat and structured, making it easier to maintain.

## How Does It Work?

1. **Create a Dependency**: Write a function or class that does a common task (like checking user permissions).
   
2. **Use It in Endpoints**: In your FastAPI routes, tell FastAPI to use this dependency with `Depends()`. FastAPI will call the function automatically and give you the result in your endpoint.

3. **Automatic Handling**: FastAPI manages all the details, so you don’t need to manually call the dependency each time.

## Examples of Using Dependency Injection:

1. **Simple Dependency**: 
   You can create a function that returns something like a mission statement. FastAPI will inject this value wherever it's needed, making your code cleaner.

2. **Dependencies with Parameters**: 
   Pass parameters (like a username) into a dependency to get specific details, such as user data, and FastAPI will take care of passing these parameters.

3. **Multiple Dependencies**: 
   You can use more than one dependency at the same time. For example, using both login verification and database connection dependencies in one endpoint.

4. **Classes as Dependencies**: 
   You can use a class to manage more complex logic and inject that class as a dependency into your endpoints.

## Benefits of Dependency Injection

- **Cleaner and Simpler Code**: Your endpoint code remains short and clear.
- **Reusability**: Write something once and use it across multiple endpoints.
- **Easier Testing**: Replace dependencies with mock objects during testing.
- **Automatic Management**: FastAPI handles the process of managing dependencies for you.

## Conclusion

Dependency Injection in FastAPI makes your code more organized, reusable, and easier to test. It helps separate concerns, allowing you to keep your application clean and maintainable. DI is an important concept in building scalable and modular applications.
