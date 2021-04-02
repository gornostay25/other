const SHEETURL = ""
const FOLDERNAME = ""

function doPost(e) {
  if (e.parameter && e.parameter.type && e.parameter.type == "callback")
  {
    Logger.log("callback "+JSON.stringify(e))
    save2Sheet("callback",{email:e.parameter.email})
  }else if(e.postData){
    let l = ""
    for (x of e.postData.contents){
      if (x != "{"){
        l+=x
      }else{
        break
      }
    }
    let params = JSON.parse(e.postData.contents.substr(l.length,parseInt(l)))
    let file = Utilities.newBlob(Utilities.base64Decode(e.postData.contents.substr(l.length+parseInt(l))),"",Math.floor(Math.random() * 10000)+"_"+params["file_name"])
    let fileurl = save2Drive(file)
    save2Sheet("form",{...params,file:fileurl})
  }
  
  Logger.log("final "+JSON.stringify(e))
  return ContentService.createTextOutput(JSON.stringify(e)).setMimeType(ContentService.MimeType.JSON)
}


function save2Drive(file){
  let foldr = []
  fol = DriveApp.getFoldersByName(FOLDERNAME)
  while (fol.hasNext()) {
    foldr.push(fol.next())
  }
  if (!foldr.length){
    foldr.push(DriveApp.createFolder(FOLDERNAME))
  }
  f = foldr[0].createFile(file)
  return f.getUrl()
}

function save2Sheet(type,data){
  let ss = SpreadsheetApp.openByUrl(SHEETURL),s;
  switch(type){
    case "callback":
      s = ss.getSheetByName("callback")
      if (!s) {
        ss.insertSheet('callback');
        s = ss.getSheetByName("callback")
        s.appendRow(["Дата","email"])
      }
      s.appendRow([new Date,data["email"]])

    break;

    case "form":
      s = ss.getSheetByName("form")
      if (!s) {
        ss.insertSheet('form');
        s = ss.getSheetByName("form")
        s.appendRow(["Дата","Имя","Тип","email","Телефон","Поручитель","Файл"])
      }
      s.appendRow([new Date,data["name"],data["rd"],data["email"],data["phone"],data["por"],data["file"]])
    break;
  }
}
