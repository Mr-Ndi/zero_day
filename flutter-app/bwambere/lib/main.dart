import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Center(
            child: Text("Sample title"),
          ),
          backgroundColor:Colors.deepPurple[400],
        ),
        body: Center(
          child: const Text("Hello World, This is a body by Ndi"),
        ),
        backgroundColor: Colors.deepPurple[100]
      ),
    ),
  );
}
