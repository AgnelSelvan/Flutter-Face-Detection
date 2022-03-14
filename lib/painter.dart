import 'dart:ui' as ui;

import 'package:flutter/material.dart';

class FacePainter extends CustomPainter {
  final ui.Image image;
  final List<List<int>> faces;
  final List<Rect> rects = [];

  FacePainter(this.image, this.faces) {
    debugPrint("Coordinates $faces");

    for (var i = 0; i < faces.length; i++) {
      final x = faces[i][0].toDouble();
      final y = faces[i][1].toDouble();
      final w = faces[i][2].toDouble();
      final h = faces[i][3].toDouble();
      final rect = ui.Rect.fromPoints(ui.Offset(x, y), ui.Offset(x + w, y + h));
      rects.add(rect);
    }
  }

  @override
  void paint(ui.Canvas canvas, ui.Size size) {
    final Paint paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.0
      ..color = const ui.Color.fromARGB(255, 255, 0, 0);

    canvas.drawImage(image, Offset.zero, Paint());
    for (var i = 0; i < faces.length; i++) {
      canvas.drawRect(rects[i], paint);
    }
  }

  @override
  bool shouldRepaint(FacePainter oldDelegate) {
    return image != oldDelegate.image || faces != oldDelegate.faces;
  }
}
