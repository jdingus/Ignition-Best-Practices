# Tags Best Practices

## Overview
Tags are a foundational part of Ignition, representing points of data that can be static or dynamic. Organizing and managing tags effectively ensures scalability, clarity, and performance.

---

## Tips and Recommendations

- **Organize Tags Logically**
  - Use folder structures to group related tags (e.g., `Production/Line1/Motors`).
  - Avoid overly deep hierarchies; keep structures manageable.

- **Use Consistent Naming Conventions**
  - Use `PascalCase` or `Title Case` for readability (e.g., `TankLevel`, `Motor Speed`).
  - Avoid special characters or spaces that might complicate scripting or integration.

- **Separate Tags by Purpose**
  - Group tags by their function, such as control, monitoring, alarms, and calculations.

- **Leverage UDTs (User-Defined Types)**
  - Use UDTs to standardize configurations and reduce duplication.
  - Update UDT definitions to propagate changes across instances.

- **Avoid Overloading Tag Providers**
  - Distribute tags across multiple providers if managing large systems.
  - Keep default tag providers lean for performance.

- **Use Memory Tags for Constants**
  - Store configuration values or static data in memory tags instead of hardcoding them.

- **Export and Version Control Tags**
  - Regularly export tags to JSON for backup and version control.
  - Commit exported tag files to a Git repository to track changes.

---

## Advanced Tips

- **Optimize Scan Classes**
  - Use scan classes strategically to balance tag polling rates and system performance.
  - Avoid excessively fast polling rates for non-critical tags.

- **Enable Tag History Wisely**
  - Use tag history sparingly for critical tags to reduce database load.
  - Configure tag history resolution and partitioning for optimal storage performance.

- **Use Expressions for Derived Tags**
  - Calculate derived values directly using expressions within tags.
  - Example: Combine multiple inputs to calculate an OEE metric.

- **Monitor Tag Performance**
  - Use Ignition's Diagnostics to monitor tag subscriptions and performance issues.
  - Clean up unused tags and bindings to optimize resources.

---

## Links to More Information
- [Tag Browser and Tag Editing](https://docs.inductiveautomation.com/display/DOC81/Tag+Browser+and+Tag+Editing)
- [Tag Historian Module](https://docs.inductiveautomation.com/display/DOC81/Tag+Historian+Module)

---
[Back to README](../README.md)
---

Feel free to contribute additional tips or corrections by submitting a pull request!
