import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Day 5 Demo',
      home: Scaffold(
        appBar: AppBar(title: Text('Day six demo')),
        body: MyHomePage(),
      ),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text('Hello World!'),
          TextField(
            onChanged: (text) {
              print('Text changed: $text');
            },
            decoration: InputDecoration(
              labelText: 'Enter text',
              border: OutlineInputBorder(),
            ),
          ),
          SizedBox(height: 10),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.star, color: Colors.amber),
              SizedBox(width: 5),
              Text('Stars Row'),
            ],
          ),
        ],
      ),
    );
  }
}
