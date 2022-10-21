package com.streetdev.final_project.covido;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;

import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class PreTest extends AppCompatActivity {

    Button start_test, cancel, call;
    TextView title, message;
    ImageView warning;
    final int ACTIVITY_TST = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pre_test);

        start_test = findViewById(R.id.start_test);
        message = findViewById(R.id.message);
        cancel = findViewById(R.id.btn_cancel);
        call = findViewById(R.id.call);

        title = findViewById(R.id.txtStart);
        warning = findViewById(R.id.ivstart);


        call.setVisibility(View.GONE);

        start_test.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PreTest.this,
                        com.streetdev.final_project.covido.Test.class);
                startActivityForResult(intent , ACTIVITY_TST);

            }
        });

        call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(PreTest.this, com.streetdev.final_project.covido.call.class);
                startActivity(intent);
                PreTest.this.finish();
            }
        });


        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                setResult(RESULT_CANCELED);
                PreTest.this.finish();

            }
        });
    }

    @SuppressLint("SetTextI18n")
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if(requestCode == ACTIVITY_TST)
        {
            if(resultCode == RESULT_OK) {
                if (data.getStringExtra("P").equals("Case")) {
                    start_test.setVisibility(View.GONE);
                    cancel.setVisibility(View.GONE);
                    call.setVisibility(View.VISIBLE);
                    title.setText("Results");
                    warning.setImageResource(R.drawable.pov);
                    message.setText(R.string.plsCall);

                }
                else {
                    start_test.setVisibility(View.GONE);
                    cancel.setVisibility(View.GONE);
                    title.setText("Results");
                    warning.setImageResource(R.drawable.ngt);
                    message.setText(R.string.SAH);
                }
            }
        }
    }
}