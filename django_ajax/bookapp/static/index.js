window.onload  = initAll;

var saveBookButton;
var showBooks;
function initAll(){
    saveBookButton=document.getElementById('save_book');
    saveBookButton.onclick = saveBook;
    showBooks = document.getElementById('profile-tab');
    showBooks.onclick= showAllBooks;


}

function saveBook(){
    var bk_name = document.getElementById('bk_name').value;
    var bk_prize = document.getElementById('bk_prize').value;
    var bk_pages = document.getElementById('bk_pages').value;
    var url = '/save_book?bk_name='+bk_name+'&bk_prize='+bk_prize+'&bk_pages='+bk_pages;
    
    var request = new XMLHttpRequest();
    request.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            if(request.responseText=='true')
            {
                document.getElementById('bk_name').value="";
                document.getElementById('bk_prize').value="";
                document.getElementById('bk_pages').value="";

            }
        }
    };
    request.open("GET", url, true);
    request.send();
}


function showAllBooks(){
    var url = '/getAllBooks'
    var request = new XMLHttpRequest();
    request.onreadystatechange=function(){
        if(this.status==200 && this.readyState==4){
            var data = eval(request.responseText);
            var div = document.getElementById('profile');
            div.innerHTML="";
            var table = document.createElement('TABLE');
            
            var row = table.insertRow(0);
            var bk_id=row.insertCell(0);
            var bk_name = row.insertCell(1);
            var bk_prize = row.insertCell(2);
            var bk_pages = row.insertCell(3);
            var bk_delete=row.insertCell(4);
            
            bk_id.innerHTML = "Serial No.";
            bk_name.innerHTML="Book Names";
            bk_prize.innerHTML="Book Prize";
            bk_pages.innerHTML = "Book Pages";
            bk_delete.innerHTML="Delete Book";
            for(var i = 0; i<data.length;i++){
                var row = table.insertRow(i+1);
                var bk_id=row.insertCell(0);
                var bk_name = row.insertCell(1);
                var bk_prize = row.insertCell(2);
                var bk_pages = row.insertCell(3);
                var bk_delete = row.insertCell(4);
                
                bk_id.innerHTML=i+1;
                bk_name.innerHTML = data[i].bk_name;
                bk_prize.innerHTML=data[i].bk_prize;
                bk_pages.innerHTML=data[i].bk_pages;
                bk_delete.innerHTML='&times';
                // bk_delete.className='text-danger'
                bk_delete.style.fontSize='30px'
                bk_delete.style.cursor='pointer'
                bk_delete.id= data[i].id;
                bk_delete.className='deleteButton';
                bk_delete.onclick=function(){
                    var obj = this;
                  var id = this.id;
                var url="/delete_book?id="+id;
                var request = new XMLHttpRequest();
                request.onreadystatechange=function(){
                      if(this.status==200 && this.readyState==4){
                         if(request.responseText=="true"){
                             table.deleteRow(obj.parentNode.rowIndex);

                         }




                      }
                  };
                  request.open("GET", url, true);
                  request.send();















                }

            }
        table.className='table text-center table-dark'
        div.append(table);
        }
    };
    request.open("GET", url, true);
    request.send();
}