package Prova.Prova_09_08.java;

import javax.jms.*;

public class MsgListener implements MessageListener {
    
    private Topic topic_t;
    private Topic topic_p;
    private TopicSession topicSession;

    public MsgListener(Topic topic_p, Topic topic_t, TopicSession topicSession) {

        this.topic_t = topic_t;
        this.topicSession = topicSession;
        this.topic_p = topic_p;
    }

    @Override
    public void onMessage(Message message) {
        
        MapMessage msg = (MapMessage) message;
        try {
            String tipo = msg.getString("type");
            TopicPublisher topicPublisher;


            if (tipo.equals("temperature")) {
                topicPublisher =topicSession.createPublisher(topic_t);
            }else {
                topicPublisher = topicSession.createPublisher(topic_p);
            }
            TextMessage text = topicSession.createTextMessage();
            Integer value = msg.getInt("value");
            text.setText(value.toString());

            topicPublisher.publish(text);

            topicPublisher.close();


        } catch (JMSException e) {
            e.printStackTrace();
        }

        
    }
}
