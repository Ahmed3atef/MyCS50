package edu.harvard.cs50.pokedex;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URL;

public class PokemonActivity extends AppCompatActivity {
    private TextView nameTextView;
    private TextView numberTextView;
    private TextView type1TextView;
    private TextView type2TextView;
    private String url;
    private RequestQueue requestQueue;
    private TextView btn_catch;
    private Integer current;
    private android.widget.ImageView imageView;
    private String ImageUrl;
    private TextView description;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pokemon);

        requestQueue = Volley.newRequestQueue(getApplicationContext());
        url = getIntent().getStringExtra("url");
        nameTextView = findViewById(R.id.pokemon_name);
        numberTextView = findViewById(R.id.pokemon_number);
        type1TextView = findViewById(R.id.pokemon_type1);
        type2TextView = findViewById(R.id.pokemon_type2);
        btn_catch = findViewById(R.id.btn_catch);
        imageView = findViewById(R.id.imag);
        description = findViewById(R.id.pokemon_description);
        load();
    }

    public void load() {
        type1TextView.setText("");
        type2TextView.setText("");
        btn_catch.setText("");

        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    nameTextView.setText(response.getString("name"));
                    numberTextView.setText(String.format("#%03d", response.getInt("id")));
                    JSONObject spritesEntry = response.getJSONObject("sprites");
                    ImageUrl = spritesEntry.getString("front_default");

                    current = response.getInt("id");

                    JSONArray typeEntries = response.getJSONArray("types");
                    for (int i = 0; i < typeEntries.length(); i++) {
                        JSONObject typeEntry = typeEntries.getJSONObject(i);
                        int slot = typeEntry.getInt("slot");
                        String type = typeEntry.getJSONObject("type").getString("name");

                        if (slot == 1) {
                            type1TextView.setText(type);
                        }
                        else if (slot == 2) {
                            type2TextView.setText(type);
                        }
                        new DownloadSpriteTask().execute(ImageUrl);
                        loadDescription();

                        String result = getPreferences(Context.MODE_PRIVATE).getString( current.toString(), "");
                        if(result.equals("")){
                            getPreferences(Context.MODE_PRIVATE).edit().putString(current.toString(), "N").commit();
                            result = "N";
                            btn_catch.setText("Catch");
                        }
                        if(result.equals("N")){
                            btn_catch.setText("Catch");
                        }else{
                            btn_catch.setText("Release");
                        }
                    }
                } catch (JSONException e) {
                    Log.e("cs50", "Pokemon json error", e);
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.e("cs50", "Pokemon details error", error);
            }
        });

        requestQueue.add(request);

    }

    private void loadDescription(){
        String url = String.format("https://pokeapi.co/api/v2/pokemon-species/%s", current.toString());
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {

                try {
                    JSONArray flavor_text_entries = response.getJSONArray("flavor_text_entries");
                    JSONObject flavor_text_entry = flavor_text_entries.getJSONObject(0);
                    description.setText(flavor_text_entry.getString("flavor_text"));
                } catch (JSONException e) {
                    Log.e("cs50", "Pokemon jason error", e);

                }
            }

            }, new Response.ErrorListener(){
                @Override
                public void onErrorResponse(VolleyError error){
                    Log.e("cs50", "Pokemon details error", error);
                }

        });
        requestQueue.add(request);
    }

    public  void toggleCatch(View view){
        Button button = findViewById(R.id.btn_catch);
        String pokemonStatus = getPreferences(Context.MODE_PRIVATE).getString(current.toString(), "");
        if(pokemonStatus.equals("N")){
            getPreferences(Context.MODE_PRIVATE).edit().putString(current.toString(), "Y").commit();
            button.setText("Release");
        }else{
            getPreferences(Context.MODE_PRIVATE).edit().putString(current.toString(), "N").commit();
            button.setText("Catch");
        }
    }

    private class DownloadSpriteTask extends AsyncTask<String, Void, Bitmap>{
        @Override
        protected Bitmap doInBackground(String... strings){
            try {
                URL url = new URL(strings[0]);
                return BitmapFactory.decodeStream(url.openStream());
            }
            catch (IOException e) {
                Log.e("cs50", "Download Sprite error", e);
                return null;
            }

        }

        @Override
        protected void onPostExecute(Bitmap bitmap){
            imageView.setImageBitmap(bitmap);
        }
    }

}
