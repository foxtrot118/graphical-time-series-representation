import { Navigate, Route } from 'react-router-dom';
import { Layout } from './components/layout';
import { NotFound } from './pages/not-found';
import { Reports } from './pages/reports';
// import uploadcsv from './components/uploadcsv';
import  Uploadcsv  from './components/Uploadcsv';




export const routes = [,
  {
    path: '/',
    element: <Navigate to="/dashboard" />
  },
  {
    path: 'csv',
    element: <Uploadcsv></Uploadcsv>
  },
  {
    path: 'dashboard',
    element: <Layout></Layout>,
    children: [
      {
        path: '/',
        element: <Reports />
      },
      {
        path: '*',
        element: <Navigate to="/404" />
      },
    ]
  },
  {
    path: '404',
    element: <NotFound />
  }
];
