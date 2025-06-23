import 'package:flutter/material.dart';
// import 'package:pixel_preview/pixel_preview.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
        appBar: AppBar(title: Text('My First App')),
        body: Center(child: Text('Hello, Flutter!')),
      ),
    );
  }
}
