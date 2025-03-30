import 'package:flutter/material.dart';

void main() {
  runApp(MyWidget());
}

class MyWidget extends StatelessWidget {
  const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Center(child: Text("Sample title")),
          backgroundColor: Colors.deepPurple[100],
        ),
        body: Center(
          child: const Image(image: AssetImage('images/image.jpeg')),
        ),
        backgroundColor: Colors.deepPurple[500],
      ),
    );
  }
}
