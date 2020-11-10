Sub graph1()
  Dim i As Long, n As Long, m As Long, j As Long, k As Long, k_min As Long, k_max As Long
  Dim GraphTitle As String
  Dim Rng As Range
  Dim msg As String
  

    
If (Worksheets("graph_generator").Range("G1") = "-") Then
    Sheets("mac graph").Activate
    With ActiveSheet
    For i = .ChartObjects.Count To 1 Step -1
    .ChartObjects(i).delete
    Next i
    End With
    Exit Sub
    ElseIf (Worksheets("mac graph").Range("B2") = "All delete") Then
    Sheets("mac graph").Activate
    With ActiveSheet
    For i = .ChartObjects.Count To 1 Step -1
    .ChartObjects(i).delete
    Next i
    End With
    Exit Sub
    ElseIf (Worksheets("mac graph").Range("B2") = "Auto") Then
        Sheets("mac graph").Activate
        With ActiveSheet
        For i = .ChartObjects.Count To 1 Step -1
        .ChartObjects(i).delete
        Next i
    End With
    ElseIf (Worksheets("mac graph").Range("B2") = "Add") Then
        Sheets("mac graph").Activate
        If (ActiveSheet.ChartObjects.Count > 1) Then
            'message box
            msg = "グラフを削除してください。"
            MsgBox msg
            Exit Sub
    End If
    End If


'エクセルの計算処理画面表示、自動計算OFF
Application.ScreenUpdating = False '
Application.Calculation = xlCalculationManual
'not vailed 11.48s 100times
'vailed 8.20s 100times


k_min = 1
k_max = Worksheets("graph_generator").Cells(Rows.Count, 2).End(xlUp).Row - 3
If (Worksheets("graph_generator").Cells(Rows.Count, 2).End(xlUp).Row - 3 <= 0) Then
            'message box
            msg = "作成するデータ範囲を入力してください。"
            MsgBox msg
            Exit Sub
            End If
 For k = k_min To k_max
 
  m = Worksheets("graph_generator").Range("C4:C103").Cells((k), 1)
  n = Worksheets("graph_generator").Range("D4:D103").Cells((k), 1)
  j = 2 + (2 * m - 1)
  
  'グラフ生成
  Sheets("mac graph").Activate
  With ActiveSheet.Shapes.AddChart2(240, xlXYScatter).Chart
    End With
    
  'グラフ位置
  Set Rng = Range(Cells((8 + 12 * (k - 1)), 3), Cells((19 + 12 * (k - 1)), 8))
  With ActiveSheet.ChartObjects(k)
  .Top = Rng.Top
  .Left = Rng.Left
  .Width = Rng.Width
  .Height = Rng.Height
  
  End With
  
  'グラフ入力
  For i = m + 1 To n + 1
  GraphTitle = Sheets("graph_generator").Range("B4:B103").Cells((k), 1).Value
    Sheets("mac graph").Activate
    With ActiveSheet.ChartObjects(k).Chart
        .HasTitle = True
        .HasLegend = True
        .ChartTitle.Text = GraphTitle
    With .Axes(xlValue)
      .HasTitle = True
      .AxisTitle.Text = "I[mA]"
    End With '.Axes(xlValue)
    With .Axes(xlCategory)
      .HasTitle = True
      .AxisTitle.Text = "V[V]"
    End With '.Axes(xlCategory)
    With .SeriesCollection.NewSeries
        Sheets("output").Activate
        .Name = Sheets("【data】").Cells(17, (i))
        .XValues = Sheets("output").Range(Cells(2, (j)), Cells(1000, (j)))
        .Values = Sheets("output").Range(Cells(2, (j + 1)), Cells(1000, (j + 1)))
        .MarkerSize = 2
        j = j + 2
    End With
    End With
    
  Next i
  Next k
  
  

  'エクセルの計算処理画面表示、自動計算ON
  Application.ScreenUpdating = True
  Application.Calculation = xlCalculationAutomatic

  
  
  Sheets("mac graph").Activate
  
  
  
End Sub




