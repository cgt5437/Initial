
<?php

/*CREATE TABLE users (
    id int(11) not null PRIMARY KEY	AUTO_INCREMENT,
    LastN varchar(50),
    FirstN varchar(50),
    side varchar(20)
);

*/


/*FOR INSETING DATA*/
if(isset($_POST['insert']))
{


	try{
	$pdoConnect= new PDO("mysql:host=localhost;dbname=hwfive","root", "" );
}
	catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }

	$fname = $_POST['fname'];
	$lname = $_POST['lname'];
	$side = $_POST['side'];


	/*MAKE SURE THAT THE Y ENTER DATA INTO ALL FIELDS*/
	if($fname==""||$lname==""||$side=="")
	{
		echo "please fill out all data";
	}
	else
	{

	$pdoQuery = "INSERT INTO `users`(`lastN`, `firstN`, `side`) VALUES (:fname,:lname,:side)";
	$pdoResult = $pdoConnect->prepare($pdoQuery);
	$pdoExec = $pdoResult->execute(array(":fname"=>$fname,":lname"=>$lname,":side"=>$side));

	
	if($pdoExec)
	{
		echo 'Data Inserted';
	}
	else
	{
		echo 'Data Not Inserted';
	}
}
	
}





?>
<!DOCTYPE html>
<html>
<head>
		<title></title>
</head>
<body>
	
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">

	Enter first name:
	<input type="text" name="fname" ><br></br>
	Enter last name:
	<input type="text" name="lname" ><br></br>
	Choose your side.  Are you a jedi or a sith? or niether?
	<input type="text" name="side" ><br></br>
	<input type="submit" name="insert" value="Insert Data"><br></br>
	<input type="submit" name="show" value="Show Data"><br></br>
	

</form>


<?php

if(isset($_POST['show']))
{
	$pdoConnect1= new PDO("mysql:host=localhost;dbname=hwfive","root", "" );
	$stmt = $pdoConnect1->query("SELECT * FROM users");
	$fNarray = array();
	$lNarray = array();
	$sideArray = array();

echo "Contents of the table in order: last name, first name, side chosen";
	while($row = $stmt->fetch())
	{
		
		echo "<br></br>";
		echo $row['firstN'];
		echo ",";
		array_push($fNarray,$row['firstN']);
		echo $row['lastN'];
		echo ",";
		array_push($lNarray,$row['lastN']);
		echo $row['side'];
		array_push($sideArray,$row['side']);	
		echo "<br></br>";	
	}

}


?>

</body>
</html>
