document.addEventListener("DOMContentLoaded", function() {
    gsap.from(".animate-navbar-js",{
        delay:0.2,
        opacity:0,
        duration:0.5,
        y:-60,
        
    
    });
    gsap.from('#right h1',{
        delay:0.2,
        opacity:0,
        duration:0.5,
        x:60,
        
    
    });
    
    gsap.from("#left",{
        delay:0.2,
        opacity:0,
        duration:0.5,
        x:-60,
    
    });
    // gsap.from("#center",{
    //     delay:0.2,
    //     opacity:0,
    //     duration:0.5,
    //     y:60,
    
    // })
    
});
//For user profile in nav
let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");
let classList = profileDropdownList.classList;
const toggle = () => classList.toggle("active");
window.addEventListener("click", function (e) {
    if (!btn.contains(e.target)) classList.remove("active");
});

function toggleMenu() {
    const menuLinks = document.getElementById("menu-links");
    menuLinks.classList.toggle("active");
}
