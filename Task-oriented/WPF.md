## Instance Binding
* Instance Binding 이 명칭은 아님
* 객체로부터 프로퍼티를 호출하여 바인딩하는 방법
* xaml에서 바인딩된 객체를 쓰고 .(dot)을 찍어 원하는 프로퍼티를 바인딩할 수 있음


```cs
public class AnyClass1
{
    public string AnyText
    {
        get { return GetProperty(() => AnyText); }
        set { SetProperty(() => AnyText, value); }
    }
}

public class AnyClass2
{
    public AnyClass1 AnyProp
    {
        get { return GetProperty(() => AnyProp); }
        set { SetProperty(() => AnyProp, value); }
    }
}
```

```cs
# MainViewModel.cs
public AnyClass2 Target
{
    get { return GetProperty(() => Target); }
    set { SetProperty(() => Target, value); }
}

# MainViewModel.cs 생성자에서 Target 초기화
Target = new AnyClass2();

```

```cs
# MainWindow.xaml
<dx:ThemedWindow.Resources>
    <DataTemplate DataType="{x:Type viewModels:MainViewModel}">
        <views:MainView/>
    </DataTemplate>
</dx:ThemedWindow.Resources>
<Grid>
    <ContentControl Content="{Binding Target}"/>
</Grid>
...

```cs
# MainView.xaml
...
    <Label Grid.Row="0" Content="BANK" VerticalContentAlignment="Center"/>
    <dxe:TextEdit Grid.Row="0" Grid.Column="1" Text="{Binding Target.AnyNum}"/>
...
...



## DataTrigger에 의한 Style 변화
```cs
<dxe:TextEdit Grid.Row="4" Grid.Column="1" IsReadOnly="True" Height="30">
    <dxe:TextEdit.Style>
        <Style TargetType="dxe:TextEdit">
            <Setter Property="Background" Value="Red" />
            <Setter Property="Text" Value="Disable"/>
            <Setter Property="Foreground" Value="White"/>
            <Setter Property="HorizontalContentAlignment" Value="Center"/>
            <Style.Triggers>
                <DataTrigger Binding="{Binding AnyClass.Var1}" Value="True">
                    <Setter Property="Background" Value="Green" />
                    <Setter Property="Text" Value="Auto"/>
                </DataTrigger>
                <DataTrigger Binding="{Binding AnyClass.Var2}" Value="True">
                    <Setter Property="Background" Value="Black" />
                    <Setter Property="Text" Value="Power Off"/>
                </DataTrigger>
            </Style.Triggers>
        </Style>
    </dxe:TextEdit.Style>
</dxe:TextEdit>
```
```cs
<Button Grid.Row="1" Grid.Column="4" Content="Move" Command="{Binding RunScenarioCommand}" CommandParameter="Move"/>
<Button Grid.Row="1" Grid.Column="5" Content="Scan" Command="{Binding RunScenarioCommand}" CommandParameter="Scan"/>
<Button Grid.Row="1" Grid.Column="6" Content="Pickup" Command="{Binding RunScenarioCommand}" CommandParameter="Pickup"/>
<Button Grid.Row="1" Grid.Column="7" Content="Unload" Command="{Binding RunScenarioCommand}" CommandParameter="Unload" />

# 아래와 같이 정의된 함수에 의해 위의 Command가 실행됨
[Command]
public void RunScenarioCommand(string msg)
```
