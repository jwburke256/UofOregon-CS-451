<?php
// processForm.php

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    echo "<pre>";
    print_r($_POST);
    echo "</pre>";
    // Capture POST data
    $manufact = $_POST['manufact'];
    $gamePublisherDropdown = $_POST['GamePublisherDropdown'];
    $platformDropdown = $_POST['PlatformDropdown'];
    $sortingDropdown = $_POST['SortingDropdown'];
    $newInput = $_POST['newInput'];

    // Display POST data for verification
    echo "<h3>POST Data Received</h3>";
    echo "<p>Manufacturer: $manufact</p>";
    echo "<p>Game/Publisher: $gamePublisherDropdown</p>";
    echo "<p>Platform: $platformDropdown</p>";
    echo "<p>Sorting Method: $sortingDropdown</p>";
    echo "<p>New Input: $newInput</p>";

    // Example: Conditional redirection to findManuCust.php
    if ($gamePublisherDropdown === 'Games') {
        // Perform any additional processing or validation as needed
        // Redirect to findManuCust.php if conditions are met
        echo '<p>Redirecting to findManuCust.php...</p>';
        // Uncomment the following line to enable redirection
        // header('Location: findManuCust.php');
        // exit;
    } else {
        echo '<p>Conditions not met. Please go back and adjust your selections.</p>';
    }
} else {
    echo '<p>No POST data received.</p>';
}
?>