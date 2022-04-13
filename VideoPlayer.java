import java.awt.*;
import java.awt.image.*;
import java.io.*;
import javax.swing.*;

public image VideoPlayer {

    private void showVideoFrame() {
        JFrame frame;
        JLabel lbIm1;
        int width = 512;
        int height = 512;
    
       // Use label to display the image
       frame = new JFrame();
       GridBagLayout gLayout = new GridBagLayout();
       frame.getContentPane().setLayout(gLayout);
    
       GridBagConstraints c = new GridBagConstraints();
       c.fill = GridBagConstraints.HORIZONTAL;
       c.anchor = GridBagConstraints.CENTER;
       c.weightx = 0.5;
       c.gridx = 0;
       c.gridy = 0;
    
       c.fill = GridBagConstraints.HORIZONTAL;
       c.gridx = 0;
       c.gridy = 1;
       frame.getContentPane().add(lbIm1, c);
    
       frame.pack();
       frame.setVisible(true);
    }

    public static void main(String[] args) {
        VideoPlayer player = new VideoPlayer();
        player.showVideoFrame();
     
    }
}