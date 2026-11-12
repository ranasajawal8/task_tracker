# Mini Task Tracker

A menu-based Python task manager built for AI Engineering, Week 1 Day 2.
Tasks are saved in `tasks.json`, so they are still there when you run the program again.

## Features

- **Add**: enter a task title; it is stored as Pending
- **View**: numbered list showing Pending or Done
- **Complete**: pick a task number to mark it Done
- **Delete**: pick a task number to remove it
- **Save and Load**: uses `json.dump()` after every change and `json.load()` at startup
- **Menu**: keeps running until you choose Exit
- **Error handling**: empty titles, invalid menu choices, invalid task numbers, and a missing (or corrupted) `tasks.json`

## How to run

```bash
python mini_task_tracker.py
```

In Google Colab, upload the file and run `!python mini_task_tracker.py`, or paste the code into a cell and call `main()`.
Note: Colab files are temporary, so download `tasks.json` or save it to Google Drive to keep your tasks.

## Example

```
--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
```

## Data format

```json
[{"title": "Read notes", "done": false}]
```
