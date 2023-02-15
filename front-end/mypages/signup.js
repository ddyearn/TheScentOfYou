$( document ).ready( function() {
    $( '.checkall' ).click( function() {
      $( '.checkbox' ).prop( 'checked', this.checked );
    } );

    $(".agreement").on("click", ".checkbox", function() {
        var is_checked = true;
    
        $(".agreement .checkbox").each(function(){
            is_checked = is_checked && $(this).is(":checked");
        });
    
        $(".checkall").prop("checked", is_checked);
    });
  } );

//   이부분 어떻게 구현하나요...
$( '.idCheck' ).click( function() {
  let userId = $('#_id').val();
  debugger;
  console.log(userId);
  $.ajax({
      url : "/scentofyou/idCheck.do",
      type : "POST",
      data : {"userId" : userId},
      success : function(data){
          if(data === "true"){
              alert("사용할 수 없는 아이디입니다.");
              $('#_id').attr('value','');
              $('#_id').focus();
          } else{
              alert("사용 가능한 아이디입니다.");
          }
      },
      error : function(){
          alert("서버요청실패");
      }
  })
} );

  $( '.pwdCheck' ).click( function() {
    var p1 = document.getElementById('pwd').value;
      var p2 = document.getElementById('pwdCheck').value;
      if(p1.length < 1) {
        alert('비밀번호를 입력하세요.');
        return false;
        }
      if(p2.length < 1) {
        alert('비밀번호를 한번 더 입력하세요.');
        return false;
        }
      if( p1 != p2 ) {
        alert("비밀번호가 일치 하지 않습니다");
        document.getElementById('pwdCheck').value='';
        document.getElementById('pwdCheck').focus();
        return false;
      } else{
        alert("비밀번호가 일치합니다");
        return true;
      }
  } );

