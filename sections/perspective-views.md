# Perspective Views Best Practices

## Overview
Perspective views are the building blocks of user interfaces in Ignition projects. Proper organization and styling ensure usability, scalability, and maintainability.

---

## Tips and Recommendations

- **View Naming Conventions**
  - Use `PascalCase` or `Title Case` for view names (e.g., `MainView` or `Main View`).

- **Property Naming**
  - Use `camelCase` starting with a lowercase letter for property names.
    - `params.publicProperty` for external-facing properties.
    - `custom.privateProperty` for internal properties.

- **Component Naming**
  - Use `PascalCase` for component names to maintain consistency (e.g., `ButtonSubmit`).

- **Page Names**
  - Use lowercase with hyphens for multi-word page names (e.g., `main-page`).

- **Style Classes**
  - Use `lowercase` with hyphens for style class names (e.g., `header-bar`).
  - Organize style classes into folders matching the view hierarchy.

- **Support Themes**
  - Set colors to use Ignition's built-in theme variables for consistency and easy theming.
  
- **Keep Views Modular**
  - Break down complex views into smaller, reusable embedded views.
  
---

## Advanced Tips

- **Event Handling**
  - Use message handlers and custom methods for centralized event logic. Avoid embedding complex logic directly in component event scripts.

- **Responsive Design**
  - Use Flex Containers to achieve responsiveness.
  - Leverage breakpoints and percentage-based sizing for mobile-friendly designs.

- **Parameter Usage**
  - Use view parameters (`params`) for passing data between embedded views.
  - Avoid hardcoding references to ensure reusability.

- **Performance Considerations**
  - Minimize bindings to reduce computation overhead.
  - Use expression bindings for lightweight calculations.
  - Cache results when dealing with high-latency data sources.

---

## Common Use Cases

- **Dashboards**
  - Use Flex Containers with evenly spaced child views for dynamic dashboards.

- **Data Entry Forms**
  - Utilize binding for validation and scripts for on-submit logic.

- **Charts and Graphs**
  - Use Ignition's built-in charting components or integrate third-party charting libraries.

---

## Links to More Information
- [Ignition Perspective Documentation](https://docs.inductiveautomation.com/display/DOC81/Perspective+Module)
- [Perspective Built-In Themes](https://docs.inductiveautomation.com/display/DOC81/Perspective+Built-In+Themes)

---
[Back to Home](../README.md)
---

Feel free to contribute additional tips or corrections by submitting a pull request!
