Sub Changes_cale_X()
Dim i As Long, max As Variant, min As Variant
    '変数取得
    max = Sheets("mac graph").Range("B5")
    min = Sheets("mac graph").Range("B6")
    
    'アクティブシート中の処置
    Sheets("mac graph").Activate
    With ActiveSheet
    For i = .ChartObjects.Count To 1 Step -1
        With .ChartObjects(i).Chart
        'max
        if(max="Auto") then
        .Axes(xlCategory).MaximumScaleIsAuto = True
        else
        .Axes(xlCategory).MaximumScale = max
        end if

        'min
        if(min="Auto") then
        .Axes(xlCategory).MinimumScaleIsAuto  = True
        else
        .Axes(xlCategory).MinimumScale = min
        end if
        
        End With
    Next i
    End With
    
End Sub

Sub Changes_cale_X()
Dim i As Long, j As Double, k As Double, L As Double
    '変数取得
    j = Sheets("mac graph").Range("B3")
    k = Sheets("mac graph").Range("B4")
    L = Sheets("mac graph").Range("B5")
    
    'アクティブシート中の処置
    Sheets("mac graph").Activate
    With ActiveSheet
    For i = .ChartObjects.Count To 1 Step -1
        With .ChartObjects(i).Chart
    '.Axes(xlValue).MaximumScale = j
    .Axes(xlCategory).MaximumScale = k
    .Axes(xlCategory).MinimumScale = L
    End With
    Next i
    End With
    
End Sub

