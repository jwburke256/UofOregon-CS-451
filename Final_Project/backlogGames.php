<?php

include('connectionData.txt');

$conn = mysqli_connect($server, $user, $pass, $dbname, $port)
or die('Error connecting to MySQL server.');

?>

<html>
<head>
  <title>HowLongToFilter</title>
  <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
            text-align: left;
	}
	button {
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #d3d3d3;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #a9a9a9;
        }
  </style>
  </head>
  
  <body bgcolor="white">
  
  
  <hr>
  
  
<?php

$gamePublisherDropdown = $_POST['GamePublisherDropdown'];
$platformDropdown = $_POST['PlatformDropdown'];
$sortingDropdown = $_POST['SortingDropdown'];

if ($gamePublisherDropdown === 'Games') {
	if ($platformDropdown === 'All') {    
		if ($sortingDropdown === 'asc_alph') {
			$query = "SELECT vg.title, na_release, dev_name, pub_name, average, median, fastest, slowest, main, main_sides, completionist FROM video_games vg ";
			$query .= "JOIN speed_runs sr USING(game_num) ";
			$query .= "JOIN completion_times ct USING(game_num) ";
    			$query .= "ORDER BY vg.title ASC;";
		}
		elseif ($sortingDropdown === 'dsc_alph') {
			$query = "SELECT vg.title, na_release, dev_name, pub_name, average, median, fastest, slowest, main, main_sides, completionist FROM video_games vg ";
			$query .= "JOIN speed_runs sr USING(game_num) ";
			$query .= "JOIN completion_times ct USING(game_num) ";
    			$query .= "ORDER BY vg.title DESC;";
		}
		elseif ($sortingDropdown === 'asc_rel') {
			$query = "SELECT vg.title, na_release, dev_name, pub_name, average, median, fastest, slowest, main, main_sides, completionist FROM video_games vg ";
			$query .= "JOIN speed_runs sr USING(game_num) ";
			$query .= "JOIN completion_times ct USING(game_num) ";
    			$query .= "ORDER BY na_release ASC;";
		}
		else { // dsc_rel
			$query = "SELECT vg.title, na_release, dev_name, pub_name, average, median, fastest, slowest, main, main_sides, completionist FROM video_games vg ";
			$query .= "JOIN speed_runs sr USING(game_num) ";
			$query .= "JOIN completion_times ct USING(game_num) ";
    			$query .= "ORDER BY na_release DESC;";	
		}

	} elseif ($platformDropdown === 'Console') {    
		if ($sortingDropdown === 'asc_alph') {
			$query = "SELECT vg.title, na_release, platforms, selected_platform, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN console_titles cg USING(game_num) ";
    			$query .= "ORDER BY vg.title ASC;";
		}
		elseif ($sortingDropdown === 'dsc_alph') {
			$query = "SELECT vg.title, na_release, platforms, selected_platform, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN console_titles cg USING(game_num) ";
			$query .= "ORDER BY vg.title DESC;";
		}
		elseif ($sortingDropdown === 'asc_rel') {
			$query = "SELECT vg.title, na_release, platforms, selected_platform, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN console_titles cg USING(game_num) ";
			$query .= "ORDER BY na_release ASC;";
		}
		else { // dsc_rel
			$query = "SELECT vg.title, na_release, platforms, selected_platform, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN console_titles cg USING(game_num) ";
			$query .= "ORDER BY na_release DESC;";	
		}
	} elseif ($platformDropdown === 'PC') {
		if ($sortingDropdown === 'asc_alph') {
			$query = "SELECT vg.title, na_release, ultrawide_supprt, hdr_support, current_price, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN pc_titles cg USING(game_num) ";
    			$query .= "ORDER BY vg.title ASC;";
		}
		elseif ($sortingDropdown === 'dsc_alph') {
			$query = "SELECT vg.title, na_release, ultrawide_supprt, hdr_support, current_price, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN pc_titles cg USING(game_num) ";
    			$query .= "ORDER BY vg.title DESC;";
		}
		elseif ($sortingDropdown === 'asc_rel') {
			$query = "SELECT vg.title, na_release, ultrawide_supprt, hdr_support, current_price, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN pc_titles cg USING(game_num) ";
    			$query .= "ORDER BY na_release ASC;";
		}
		else { // dsc_rel
			$query = "SELECT vg.title, na_release, ultrawide_supprt, hdr_support, current_price, dev_name, pub_name FROM video_games vg ";
			$query .= "RIGHT JOIN pc_titles cg USING(game_num) ";
    			$query .= "ORDER BY na_release DESC;";	
		}
	}
} elseif ($gamePublisherDropdown === 'Publisher') {
	$query = "SELECT * FROM how_long_to_filter.publisher ";
	$query .= "ORDER BY pub_name ASC;";	
} elseif ($gamePublisherDropdown === 'wiki') {
	$query = "SELECT title, url FROM how_long_to_filter.ign_wiki ";
	$query .= "ORDER BY title ASC;";	
}

?>

<p>
The query:
<p>
<?php
print $query;
?>

<hr>
<p>
Result of query:
<p>

<?php
$result = mysqli_query($conn, $query)
or die(mysqli_error($conn));

?>
<table>
        <tr>
            <?php
            // Fetch field names and create table headers
            if ($result->num_rows > 0) {
                $fields = $result->fetch_fields();
                foreach ($fields as $field) {
                    echo "<th>" . htmlspecialchars($field->name) . "</th>";
                }
            }
            ?>
        </tr>
        <?php
        // Output data of each row
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
		foreach ($row as $key => $cell) {
                	echo "<td>";
                	if ($key == 'url') {
                    		echo "<a href='" . htmlspecialchars($cell) . "'>" . htmlspecialchars($cell) . "</a>";
                	} else {
                    		echo htmlspecialchars($cell);
                	}
		echo "</td>";
		}
            }
        } else {
            echo "<tr><td colspan='" . count($fields) . "'>No results found</td></tr>";
        }
        ?>
</table>

<hr>

<button onclick="goBack()">Back</button>
<script>
	function goBack() {
		window.location.href = "http://ix.cs.uoregon.edu/~jburke2/HowLongToFilter/index.html";
	}
</script>

<?php
mysqli_free_result($result);

mysqli_close($conn);

?>
 
</body>
</html>
	  
