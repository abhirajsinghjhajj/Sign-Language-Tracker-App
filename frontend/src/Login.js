import HeaderLogin from "./HeaderLogin";
import React from "react";
function Login(props)
{
    const setlogin = props.setlogin;
    function loginHandler()
    {
        setlogin(true);
    }
    return(
        <div className="flex flex-col justify-between items-center  h-screen w-[90vw] mx-auto mt-4 mb-4">
            <HeaderLogin></HeaderLogin>
            <div className="flex flex-col items-center justify-center border-2 border-gray-300 p-5 rounded-xl shadow-lg shadow-cyan-500/50 ">
            <h1 className="text-bold text-2xl  py-2">Welcome to <span className="text-blue-500 font-semibold">Prototype testing</span></h1>
            <p className="italic text-sm">Designed bu 'TEAM 007'</p>
            <button onClick={loginHandler} className="border-2 border-black text-white bg-blue-500 py-1 px-3 rounded-xl mt-5 mb-1">Continue..</button>
            </div>  
            <div className="text-sm flex items-center"><span>©</span><span>opyright<span>  </span>"TEAM 007"</span></div>
        </div>
    )
};

export default Login;