import { useState } from "react";
import "./App.css";
import Login from "./Login";
import Main from "./Main";
function App() {
   const [login,setlogin] = useState(false);
   return(
      <div className=" h-screen w-full flex flex-col items-center ">
         {
            login ? <Main></Main> : <Login login={login} setlogin = {setlogin}></Login>
         }
      </div>
   )   
}

export default App;
