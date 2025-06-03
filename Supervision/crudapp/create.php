<?php
require 'db.php';

$message = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name    = $_POST['name'];
    $age     = $_POST['age'];
    $grade   = $_POST['grade'];
    $email   = $_POST['email'];
    $phone   = $_POST['phone'];
    $address = $_POST['address'];

    $sql = "INSERT INTO students (name, age, grade, email, phone, address)
            VALUES (:name, :age, :grade, :email, :phone, :address)";

    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':name'    => $name,
        ':age'     => $age,
        ':grade'   => $grade,
        ':email'   => $email,
        ':phone'   => $phone,
        ':address' => $address
    ]);

    $message = "Student added successfully!";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Add Student</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h2>Add Student</h2>
    <?php if ($message): ?>
        <p style="color: green;"><?php echo $message; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <input type="text" name="name" placeholder="Full Name" required><br><br>
        <input type="number" name="age" placeholder="Age" required><br><br>
        <input type="text" name="grade" placeholder="Grade/Class" required><br><br>
        <input type="email" name="email" placeholder="Email" required><br><br>
        <input type="text" name="phone" placeholder="Phone" required><br><br>
        <textarea name="address" placeholder="Address" required></textarea><br><br>
        <button type="submit">Add Student</button>
    </form>
    <br>
    <a href="index.php">View All Students</a>
</body>
</html>
