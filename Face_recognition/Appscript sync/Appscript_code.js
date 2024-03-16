function getAllData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  var sheet = ss.getActiveSheet();

  var firebaseUrl = "https://faceattendancesystem-8c19d-default-rtdb.firebaseio.com/Students";
  var base = FirebaseApp.getDatabaseByUrl(firebaseUrl);

  var data = base.getData();
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.clear();
  
  // set the header row 1
  
  var headers = ["BRANCH", "NAME", "TOTAL_ATTENDANCE","LAST_ATTENDANCE_TIME" ];
 
  sheet.appendRow(headers);
  
  
  
  // loop through the Firebase data and write to sheet
  for (var key in data) {
    var row = data[key];
    var rowData = [row.Branch, row.name,row.total_attendance,row.last_attendance_time];
    sheet.appendRow(rowData);
    Logger.log(rowData);
  }
