import React, { useEffect, useState } from 'react';
import './App.css'

const API_URL = 
const ApiCall = async(API_URL) => {
  try{
    const response = await fetch(API_URL);
    const data = await response.text();
    console.log('API Response:', data);
    return data;
  } catch (error) {
    console.error("Error fetching data", error);
    throw error;
  }
}

const ApiPrint = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const jsonData = await ApiCall();
        setData(jsonData);
      } catch (error) {
        console.error("Error setting data", error);
      }
  };

  fetchData();
},[]);

  return (
    <div>
      <h1>Json Data: </h1>
      <pre>{data}</pre>
    </div>
  )
    };

    export default ApiPrint;