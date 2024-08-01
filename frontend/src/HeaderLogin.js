import React from "react";
function HeaderLogin()
{
    return(
        <div className="flex flex-wrap justify-between max-w-[1180px] mx-auto w-[90vw] items-center gap-y-3 ">
            <div className="font-bold text-xl max-md:mx-auto">TEAM 007</div>
            <div className="flex gap-5 justify-center items-center max-md:mx-auto">
                <span className="border-2 border-slate-200 py-2 px-2 rounded-lg text-sm cursor-pointer">About Us</span>
                <span className="border-2 border-slate-200 py-2 px-2 rounded-lg text-sm cursor-pointer">Contact Us</span>
            </div>
        </div>
    )
};
export default HeaderLogin;