package com.streetdev.final_project.covido;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class Country_dial extends AppCompatActivity {
    private TextView country, number;
    private ImageView dial;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_country_dial);

        String name = getIntent().getStringExtra("name");
        String num = getIntent().getStringExtra("number");


        country = findViewById(R.id.country);
        number = findViewById(R.id.number);
        dial = findViewById(R.id.dial);

        country.setText(name);
        number.setText(num);

        dial.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + num) );
                startActivity(intent);



            }
        });

    }
}