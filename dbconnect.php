<?php

class User extends Dbh{

	public function getFirstN(){


	
	$stmt = $this->connect()->query("SELECT * FROM users");

	while($row = $stmt->fetch())
	{

		echo $row['firstN'];
		

	}
}


	public function getUserInfoCarefully(){




	}
}


?>




<?php


class Dbh {
private $servername;
private $username;
private $password;
private $dbname;
private $charset;

public function connect(){
	$this->servername = "localhost";
	$this->username = "root";
	$this->password = "";
	$this->dbname = "hwfive";
	$this->charset = "utf8mb4";

	try {
	$dsn = "mysql:host=".$this->servername.";dbname=".$this->dbname.";charset".$this->charset;
	
	$pdo = new PDO($dsn,$this->username, $this->password );
	return $pdo;
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully"; 
    }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
}


}


	
	echo $fname;



?>
