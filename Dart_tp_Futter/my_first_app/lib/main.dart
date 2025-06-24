import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(home: MyHomePage()));
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _controller = TextEditingController();
  final List<String> _plans = [];

  void _addPlan() {
    final text = _controller.text;
    if (text.isNotEmpty) {
      setState(() {
        _plans.add(text);
        _controller.clear(); // clear input after adding
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Plan Pulse')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(
                labelText: 'Enter your plan',
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(onPressed: _addPlan, child: Text('Add Plan')),
            SizedBox(height: 20),
            Expanded(
              child: ListView.builder(
                itemCount: _plans.length,
                itemBuilder: (context, index) {
                  return ListTile(title: Text(_plans[index]));
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
