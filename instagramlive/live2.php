<?php
set_time_limit(0);
date_default_timezone_set('UTC');
require __DIR__.'/vendor/autoload.php';
$ig = new \InstagramAPI\Instagram();
try {
    $ig->login('vovkoleg12', '123456qwerty');
} catch (\Exception $e) {
    echo 'Something went wrong: '.$e->getMessage()."\n";
    exit(0);
}/*
    $stream = $ig->live->create();
    $broadcastId = $stream->getBroadcastId();
    $ig->live->start($broadcastId);
    $streamUploadUrl = $stream->getUploadUrl();
 */

	$stream = $ig->live->create();

            $broadcastId = $stream->getBroadcastId();
            $streamUploadUrl = $stream->getUploadUrl();
$ig->live->start($broadcastId);
            //Split the stream key from the stream url
            $split = preg_split("[" . $broadcastId . "]", $streamUploadUrl);
            $streamUrl = trim($split[0]);
            $streamKey = trim($broadcastId . $split[1]);
    echo($streamUploadUrl);


?>
