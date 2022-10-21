package com.streetdev.final_project.covido;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;

import javax.xml.transform.Result;

public class Test extends AppCompatActivity {

    TextView tvAsk;
    Button ts_yes, ts_No, ts_dont;
    private int counter = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test);

        tvAsk = findViewById(R.id.tv_ask);
        ts_yes = findViewById(R.id.ts_yes);
        ts_No = findViewById(R.id.ts_no);
        ts_dont = findViewById(R.id.ts_dont);

        tvAsk.setText(R.string.ask1);


        ts_yes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                counter ++;

                if (counter == 1){
                    ts_dont.setVisibility(View.GONE);
                    tvAsk.setText(R.string.ask2);
                }
                else if (counter == 2){

                    String data = "Case";
                    Intent intent = new Intent();
                    intent.putExtra("P", data);
                    setResult(RESULT_OK,intent);
                    Test.this.finish();

                }
                else if (counter == 3){

                    tvAsk.setText(R.string.ask5);
                }
                else if (counter == 4){
                    String data = "Case";
                    Intent intent = new Intent();
                    intent.putExtra("P", data);
                    setResult(RESULT_OK,intent);
                    Test.this.finish();

                }

            }
        });

        ts_No.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                counter ++;

                if (counter == 1){
                    ts_dont.setVisibility(View.GONE);
                    tvAsk.setText(R.string.ask2);

                }
                else if (counter == 2){

                    tvAsk.setText(R.string.ask4);
                }
                else if (counter == 3){
                    tvAsk.setText(R.string.ask5);

                }
                else if (counter == 4){
                    String data = "notCase";
                    Intent intent = new Intent();
                    intent.putExtra("P", data);
                    setResult(RESULT_OK, intent);
                    Test.this.finish();


                }
            }
        });

        ts_dont.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                counter ++;
                ts_dont.setVisibility(View.GONE);
                tvAsk.setText(R.string.ask2);
            }
        });
    }
}