<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple To-Do App</title>
</head>
<body>

    <h1>To-Do List</h1>

    <form action="{{ route('tasks.store') }}" method="POST">
        @csrf
        <input type="text" name="name" placeholder="New Task" required>
        <button type="submit">Add</button>
    </form>

    <ul>
        @foreach ($tasks as $task)
            <li>
                {{ $task->name }}
                <form action="{{ route('tasks.destroy', $task) }}" method="POST" style="display:inline">
                    @csrf
                    @method('DELETE')
                    <button type="submit">Delete</button>
                </form>
            </li>
        @endforeach
    </ul>

</body>
</html>
