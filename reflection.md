# PawPal+ Project Reflection

## 1. System Design
i. Add and manage pet care tasks
    Create, edit, or delete tasks like feeding, walks, medication, grooming, etc., including details such as duration and priority.
ii. Generate a daily care schedule
    Automatically create a daily plan based on available time, task priorities, and user preferences.
iii. View today’s plan with explanations
    See a clear list of scheduled tasks for the day along with reasoning (e.g., why certain tasks were prioritized or scheduled at specific times).

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design for PawPal+ included five main classes with the following responsibilities:

Task – Represents a pet care activity. It stores information such as name, duration, priority, associated pet, and optional time window. It can update its details, check if it fits in available time, and provide a readable description.
Pet – Represents a pet. It stores basic information (name, species, age) and a list of tasks. It can add, remove, or list tasks for the pet.
Owner – Represents the pet owner. It stores the owner’s name, available time, preferences, and the list of pets. It can add pets, update preferences, and provide the owner’s available time for scheduling.
Schedule – Represents a daily plan for the owner. It stores the date, owner, scheduled tasks, and explanations for decisions. It can generate the plan, add or remove tasks, explain scheduling choices, and display the schedule clearly.
Scheduler – Acts as the logic engine to create schedules. It can sort tasks by priority, fit tasks into the day, resolve conflicts, and generate a complete daily schedule for an owner.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Change 1: Owner ↔ Pet bidirectional link

Problem: Pet doesn’t know which Owner it belongs to, so navigating from a Pet to its Owner (for scheduling or preference checks) is impossible.
Solution: Add an owner attribute to Pet

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
