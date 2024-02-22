// Obtenir le token
// const myHeaders = new Headers({
//   "Content-Type": "application/json",
// });

// const raw = JSON.stringify({
//   username: "jcemopeno-bia@linkuup.net",
//   password: "8Uu!S24kBQaXkqH",
// });

// const requestOptions = {
//   method: "POST",
//   headers: myHeaders,
//   body: raw,
//   redirect: "follow",
// };

// fetch("https://production.api-annuaire-sante.fr/login_check", requestOptions)
//   .then((response) => response.json())
//   .then((result) => {
//     const token = result.token; // Stocker le token dans une variable locale
//     console.log(token);
//     // Stocker le token dans le localStorage
//     //localStorage.setItem("token", token);
    
//     // Utiliser le token ici

    
//   })
//   .catch((err) => console.log("err: ", err));

const fs = require('fs');
// const fetch = require('node-fetch');

// Utilisation de import() pour importer node-fetch de manière dynamique
import('node-fetch').then(fetch => {
  const token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MDcyOTM3OTcsImV4cCI6MTcwNzI5NzM5Nywicm9sZXMiOlsiUk9MRV9VU0VSIl0sInVzZXJuYW1lIjoiamNlbW9wZW5vLWJpYUBsaW5rdXVwLm5ldCJ9.ayA-q4TuWNKaz4sJ2ktAolYHEPBmLKFJhRs8wcLuq_X_bh5t5-TGpfdCzM17kvxDqveojp-GujZIxqvA3w_xIFQDvRP8uY4r7LUmq-vVRcp89iPdq-ns8JeOq2UFSYuH4U5XLgEuKSrjNzq04OwXD30P9x-lbTTC-3c7zkASklVgqDIURDyNySeBOZAlfblAp3cN_g3s9o9Wsl-OgzhM__z6b5QnqGuny5coBDsyicUatLrbprxZAiHh_HfBG6NuHhHOw0HdRppM_qvE0GDbAPP-2iLeigQcgg_luAa0Aoea6rrkeUs7qAWTMirQ0bO_Cuix7DSSKU2h3LV3XzAn60rZZP_9xodFuOnz64VX7ZQxdJvzvuKYmLZf9DUm48PxdNxTGBFZ9bvzq7EJ4E1d6P6HKvygH3VFCEBHSzacCNL8cRpvsHUKreEQOzWmwCwBJHgjnx6Wc2Rr0J0eOglCd73XcmMi9oUvq_h2zN12lFVRAGE9J-aCxR6vLlXZE9AvzGeuXTi5tznp_os3ZbdIzjD8mDAH8WhaQ7ZTku09iIG7smkU5X1Y_rEFM-YNoLgZZGyZngM2AyAsvdsvlFKk7JP6mIGvFGDKiRYNdWVFPvBQ9PZI44HTa_0o993HS2qHZSAOIhYKr6goWVpgZtbpzfObkFBCPwjzN8WzvTsD5n8";

  const myHeaders1 = new fetch.Headers({
    Authorization: "Bearer " + token,
  });

  const requestOptions1 = {
    method: "GET",
    headers: myHeaders1,
    redirect: "follow",
  };

  fetch.default("https://production.api-annuaire-sante.fr/professionnel_de_santes?libelleProfession[]=Médecin", requestOptions1)
    .then(response => response.json())
    .then(result => {
      console.log(result);
      // Storing the result in a file
      fs.writeFile('result.json', JSON.stringify(result), err => {
        if (err) {
          console.error('Error writing file:', err);
          return;
        }
        console.log('Result has been stored in result.json');
      });
    })
    .catch(err => console.error("Error fetching data:", err));
});
