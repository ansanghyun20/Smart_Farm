<!DOCTYPE html>
<html>


<body>

<div id="sample">
<meta name = "viewport" content= "user-scalable=no, initial-scale=2.0, maxium-scale=2.0, minimum-scale=2.0, width=device-width" />
<?php

  //php info
  $mysql_hostname = 'localhost';
  $mysql_username = 'root';
  $mysql_password = '0000';
  $mysql_database = 'AutoFarming';

  //DB연결
  $connect = new mysqli($mysql_hostname, $mysql_username, $mysql_password, $mysql_database);
  //DB연결 확인
  if($connect->connect_errno){
 echo '[연결실패] : '.$connect->connect_error.'<br>';
  } else {
 echo '[연결성공]<br>';
  }
   $humidity = $_GET['Humid'];         //습도 읽어와
   $temperature = $_GET['Temp'];   //온도 읽어와

 $query3 = "SELECT * FROM Status ORDER BY ID DESC LIMIT 1";
    $result = $connect->query($query3);  //쿼리실행
    $row = mysqli_fetch_object($result); //실행된 쿼리값을 읽음


echo 'Temperature : '. $row->Temp. '<br>';
echo 'Humid : '. $row->Humid. '<br>';
echo 'Light : '. $row->Light. '<br>';
echo 'Time : '.  $row->CTime. '<br>'; 





?>
</div>


</body>

<body>
</body>


</html>


<script language='javascript'>
  window.setTimeout('window.location.reload()',500); //1초마다 리플리쉬 시킨다 1000이 1초가 된다.
</script>
