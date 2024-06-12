const allFilterItems = document.querySelectorAll('.box');
const allFilterBtns = document.querySelectorAll('.filters-btn');

window.addEventListener('DOMContentLoaded', () => {allFilterBtns[0].classList.add('active-btn');});

allFilterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
        showFilteredContent(btn);
    });
});

function showFilteredContent(btn){
    allFilterItems.forEach((item) => {
        if(item.classList.contains(btn.id)){
            resetActiveBtn();
            btn.classList.add('active-btn');
            item.style.display = "block";
        } else {
            item.style.display ="none";
        }
    });
}

function resetActiveBtn(){
    allFilterBtns.forEach((btn) => {
        btn.classList.remove('active-btn');
    });
}

function showSidebar() {
    document.querySelector('.sidebar').style.display = 'flex';
  }

  function closeSidebar() {
    document.querySelector('.sidebar').style.display = 'none';
  }


const navlink=document.querySelectorAll('.navitems');

navlink.forEach(navlinkel=>{
    navlinkel.addEventListener('click',()=>{
        navlinkel.classList.add('active');
    })
})