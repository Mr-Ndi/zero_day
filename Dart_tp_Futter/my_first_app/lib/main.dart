import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Day 6 - Input & Button',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: InputExampleScreen(),
    );
  }
}

class InputExampleScreen extends StatefulWidget {
  @override
  _InputExampleScreenState createState() => _InputExampleScreenState();
}

class _InputExampleScreenState extends State<InputExampleScreen> {
  final TextEditingController _nameController = TextEditingController();
  String _greeting = '';
  String? _errorText;

  void _sayHello() {
    final name = _nameController.text.trim();
    if (name.isEmpty) {
      setState(() {
        _errorText = 'Please enter your name';
        _greeting = '';
      });
    } else {
      setState(() {
        _greeting = '👋 Hello, $name!';
        _errorText = null;
        _nameController.clear(); // clear the input field
      });
    }
  }

  @override
  void dispose() {
    _nameController.dispose(); // clean up controller
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Day 6: Inputs & Buttons')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _nameController,
              decoration: InputDecoration(
                labelText: 'Enter your name',
                border: OutlineInputBorder(),
                errorText: _errorText,
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(onPressed: _sayHello, child: Text('Say Hello')),
            SizedBox(height: 24),
            Text(_greeting, style: TextStyle(fontSize: 24)),
          ],
        ),
      ),
    );
  }
}
