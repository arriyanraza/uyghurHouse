const supabaseConfig = {
    url: process.env.NEXT_PUBLIC_SUPABASE_URL,
    key: process.env.NEXT_PUBLIC_SUPABASE_KEY
};

console.log(supabaseConfig);

export default supabaseConfig;