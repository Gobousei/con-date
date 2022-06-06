function doGet(e) {
const htmlOutput = HtmlService.createTemplateFromFile("index").evaluate();
  htmlOutput
    .setTitle('con-date')
    .setFaviconUrl('https://raw.githubusercontent.com/Gobousei/con-date/main/rice.png');
  return htmlOutput;
}

function getAppUrl() {
  return ScriptApp.getService().getUrl();
}
function doSubmitAjax(req) {
    const params = req.parameters;
    const resObj = {};
    //この1行を追加
    insertRecord(params);
    return resObj;
  }
    function insertRecord(param){
    let reservationTime = 0;
    const fromDate = new Date(param.calendar_date_from +' ' + param.calendar_time_from);
    const toDate = new Date(param.calendar_date_to + ' ' + param.calendar_time_to);

    //この順番にスプレッドシートに格納される
    const data = [[
      param.user_id, 
      param.user_name, 
      param.calendar_date_from,
      param.calendar_time_from,
      param.calendar_time_to,
      param.url,
      param.comments,
      new Date()
    ]];
    //SPREAD_SHEET_IDは連携するスプレッドシートのID、SHEET_NAMEはシート名をそれぞれ置き換えてください。
    const app = SpreadsheetApp.openById('1mBJh_XaPoGlWDpTIHScZidZt6r8SFXJajwK_AHk1W1o');
    const sheet = app.getSheetByName('database');
    const insertRow = sheet.getDataRange().getLastRow() + 1;  //挿入行
    const insertCol = 1;  //挿入列
    const insertRowNum = data.length;  //挿入行数
    const insertColNum = data[0].length;  //挿入列数(データ数)
    const insertRange = sheet.getRange(insertRow, insertCol,insertRowNum,insertColNum);
    //スプレッドシートに書きこむAPI
    insertRange.setValues(data);
  }
