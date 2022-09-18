// import { useRoutes } from 'react-router-dom';
// import { CssBaseline, ThemeProvider } from '@material-ui/core';
// import { theme } from './theme';
// import { routes } from './routes';
// import './app.css';
// import timeseries from './charts/timeseries';



// // const App = () => {
// //   const content = useRoutes(routes);

// //   return (
// //       <ThemeProvider theme={theme}>
// //         <CssBaseline />
// //         {content}
// //       </ThemeProvider>
// //   );
// // };

// // export default App;
// function App() {
//   const content = useRoutes(routes);

//   return (
//     <div className="App">
//     <h2> TIME SERIES REPRESENTATION</h2>
//     <div className='row'>
//     <ThemeProvider theme={theme}>
//          <CssBaseline />
//          {content}
//        </ThemeProvider>

//        <timeseries width={400} height={300}/>
//       <routes/>

      
//     </div>
//     </div>
//   );
// }

// export default App;
import { useRoutes } from 'react-router-dom';
import { CssBaseline, ThemeProvider } from '@material-ui/core';
import { theme } from './theme';
import { routes } from './routes';
import React, { useState, useEffect } from 'react';
import TimeSeries from './charts/timeseries';
import Histogram from './charts/Histogram';
import './app.css';



// const App = () => {
//   const content = useRoutes(routes);

//   return (
    
//       <ThemeProvider theme={theme}>
//         <CssBaseline />
//         {content}
//       </ThemeProvider>
//   );
// };

// export default App;
function App() {
  const content = useRoutes(routes);

  return (
    <div className="App">
    <h2> TIME SERIES REPRESENTATION</h2>
    <div className='row'>
    <ThemeProvider theme={theme}>
         <CssBaseline />
         {content}
       </ThemeProvider>

      <TimeSeries width={400} height={300}/>
      <Histogram width={400} height={400}/>
      <routes/>

      
    </div>
    </div>
  );
}

export default App;

