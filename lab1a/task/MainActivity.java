package com.example.mnd_labwork_1a;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @SuppressLint("SetTextI18n")
    public void click(View view){
        EditText edNumber = findViewById(R.id.textInputEditText);
        TextView text = findViewById(R.id.textView);
        TextView text1 = findViewById(R.id.textView1);
        try {
            int number = Integer.parseInt(edNumber.getText().toString());
            if (number % 2 == 0) {
                text.setText((number / 2 + "*" + "2"));
            } else {
                int x = (int) Math.ceil((Math.sqrt(number)));
                while (!(Math.pow((int) Math.sqrt(x * x - number), 2) == x * x - number)) {
                    x += 1;
                    System.out.println(x);
                }
                int y = (int) Math.sqrt(x * x - number);
                text.setText((x - y) + "*" + (x + y));
                text1.setText("Кількість проведених ітерацій: " +  x);
            }
        }
        catch (Exception e){
            text.setText("Сталася помилка!");
        }
    }

}