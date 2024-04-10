import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}



const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await new Promise((resolve, reject) => {
            client.get(schoolName, (err, reply) => {
                if (err) reject(err);
                resolve(reply);
            });
        });
        
        console.log(value);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}: ${error}`);
    }
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
