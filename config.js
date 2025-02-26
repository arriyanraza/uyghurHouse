// Supabase configuration
// Copy this file to config.js and update with your credentials
export const supabaseUrl = process.env.SUPABASE_URL || "PLACEHOLDER_URL";
export const supabaseKey = process.env.SUPABASE_KEY || "PLACEHOLDER_KEY";

const supabaseConfig = {
    url: supabaseUrl,
    key: supabaseKey
};
