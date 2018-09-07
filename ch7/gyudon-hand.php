<?php
$self = "gyudon-hand.php";
$base_dir = dirname(__FILE__). "/image";
$unknown_dir = "gyudon";
$dirs = array(
  "普通の牛丼" => "normal",
  "紅ショウガ牛丼" => "beni",
  "ねぎ玉牛丼" => "negi",
  "チーズ牛丼" => "cheese",
  "キムチ牛丼" => "kimuti",
  "その他" => "other",
);
// 必要なディレクトリを作成
foreach ($dirs as $key => $dir) {
  $path = $base_dir."/$dir";
  if (!file_exists($path)) {
    mkdir($path); chmod($path, 0777);
  }
}
// 振り分けるか、それとも、フォームを表示するか 
$m = isset($_GET["m"]) ? $_GET["m"] : "";
if ($m == "mv") { // 振り分け
  $target = $_GET["target"]; // パラメータの取得
  $to = $_GET["to"];
  $path = $base_dir."/$unknown_dir/$target";
  // パラメータのチェック
  if ($target == "") { echo "error..."; exit; }
  if (!file_exists($path)) {
    echo "<a href='$self'>already ...</a>"; exit;
  }
  if (!file_exists("$base_dir/$to")) {
    echo "system error : no dir $to"; exit;
  }
  // ファイルの移動(念のためコピーしてから削除)
  $path_to = "$base_dir/$to/$target";
  copy($path, $path_to);
  if (file_exists($path_to)) {
    unlink($path);
  } else {
    echo "Sorry, could not move."; exit;
  }
  // 選択画面にリダイレクト
  header("location: $self");
  echo "<a href='$self'>Thank you, moved.</a>";
} else {
  // 牛丼の選択フォームを表示
  $files = glob("$base_dir/$unknown_dir/*.jpg"); // 画像列挙
  if (count($files) == 0) {
    echo "<h1>完了です!</h1>"; exit;
  }
  shuffle($files); // 適当なファイルを選ぶ
  $target = basename($files[0]); 
  $remain = count($files); // 残りのファイル数
  $buttons = ""; // 選択肢の生成
  foreach ($dirs as $key => $dir) {
    $fs = glob("$base_dir/$dir/*.jpg"); // 振り分けたファイル数
    $cnt = count($fs);
    $api = "$self?m=mv&target=$target&to=$dir";
    $buttons .= "[<a href='$api'>$key($cnt)</a>] ";
  }
  echo <<< EOS
    <html><head><meta charset="utf-8">
      <meta name="viewport" content="width=320px">
      <style> body { text-align:center;
                     font-size: 24px; }
      </style></head><body>
      <h3 style="font-size:12px">選んでください(残り:$remain)</h3>
      <img src="./image/$unknown_dir/$target" width=300><br>
      $buttons
    </body></html>
EOS;
}

