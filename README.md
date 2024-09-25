# ToDo
Website designed to help users efficiently organise and manage their tasks. It features a user-friendly interface where users can create, view, and manage their to-do items.
Key functionalities include:

# Task Display and Filtering:

Tasks are displayed in a card format with details such as title, description, and date.
Users can filter tasks based on their status: active, completed, or all, using buttons provided at the top of the task list.

#Task Completion and Removal:

Users can mark tasks as completed by clicking a "Complete" button on each task card. Completed tasks will no longer display the "Complete" button.
Users can also remove tasks using the "Remove" button, which deletes the task from the list.

# Dynamic Updates:

The site uses JavaScript to handle task completion without reloading the page. AJAX requests are used to send completion data to the server, and the task list is updated dynamically to reflect changes immediately.
Completed tasks are visually distinguished and the "Complete" button is removed to indicate the change.
# Server-Side Integration:

The site integrates with a Django backend to handle data storage and management.
Tasks are fetched, updated, and removed using Django views and URL routes, ensuring seamless interaction between the frontend and backend.

Overall, the to-do management site provides a streamlined and intuitive experience for managing everyday tasks, helping users stay organized and productive.
